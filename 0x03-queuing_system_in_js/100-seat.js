import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const kue = require('kue');
const queue = kue.createQueue();

const client = redis.createClient();
const clientGet = promisify(client.get).bind(client);

let reservationEnabled = true;

function reserveSeat (number) {
  client.set('available_seats', number);
}

async function getCurrentAvailableSeats () {
  return await clientGet('available_seats');
}

const app = express();
reserveSeat(50);

app.get('/available_seats', async (req, res) => {
  const seats = await getCurrentAvailableSeats();
  res.send({ numberOfAvailableSeats: seats });
});

app.get('/reserve_seat', (req, res) => {
  if (reservationEnabled === false) {
    res.send({ status: 'Reservation are blocked' });
  }
  const job = queue.create('reserve_seat');
  job.save((error) => {
    if (!error) res.send({ status: 'Reservation in process' });
    if (error) res.send({ status: 'Reservation failed' });
  });

  job.on('complete', () => console.log(`Seat reservation job ${job.id} completed`));
  job.on('failed', (error) => console.log(`Seat reservation job ${job.id} failed: ${error}`));
});

app.get('/process', (req, res) => {
  queue.process('reserve_seat', async (job, done) => {
    const newAvailableSeats = await getCurrentAvailableSeats() - 1;
    reserveSeat(newAvailableSeats);
    if (newAvailableSeats === 0) reservationEnabled = false;
    if (newAvailableSeats > 0) done();

    done(new Error('Not enough seats available'));
  });
  res.send({ status: 'Queue processing' });
});

app.listen(1245);
