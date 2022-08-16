import redis, { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool (schoolName, value) {
  client.set(schoolName, value, (err, resp) => {
    if (err) console.log(err);
    redis.print(resp);
  });
}

function displaySchoolValue (schoolName) {
  client.get(schoolName, (err, resp) => {
    if (err) console.log(err);
    console.log(resp);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
