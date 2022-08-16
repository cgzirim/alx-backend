import redis from 'redis';
import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', (err) => console.log('Redis Client Error', err));

const subscriber = client.duplicate();

// subscriber.subscribe('holberton school channel', (err, count) => {
//     console.log(count)
// })

subscriber.subscribe('holberton school channel')


subscriber.on('message', (channel, message) => {
    console.log(message)
    if (message === 'KILL_SERVER') {
        subscriber.unsubscribe('holberton school channel')
        subscriber.quit()
    }
})
