import redis, { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
client.on('connect', () => console.log('Redis client connected to the server'));

const keys = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
const values = [50, 80, 20, 20, 40, 2];

keys.forEach((key, index) => {
  client.hset('HolbertonSchools', key, values[index], redis.print);
});

client.hgetall('HolbertonSchools', (err, resp) => {
  if (err) console.log(err);
  console.log(resp);
});
