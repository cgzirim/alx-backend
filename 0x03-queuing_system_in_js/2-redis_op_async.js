import redis from 'redis';
const util = require('util');
import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', (err) => console.log('Redis Client Error', err));

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
        if (err) {
            console.log(err);
        }
        redis.print(reply);
    })
}

const setNewSchoolAsync = util.promisify(client.set).bind(client);

async function displaySchoolValue(schoolName) {
    const resp = await client.get(schoolName);
    console.log(resp);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');