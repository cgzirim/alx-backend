import express from 'express'
import redis from 'redis'
import { promisify } from 'util'

const client = redis.createClient();
const clientGet = promisify(client.get).bind(client);
const clientSet = promisify(client.set).bind(client);

const listProducts = [
    {Id: 1, name: "Suitcase 250", price: 50, stock: 4},
    {Id: 2, name: "Suitcase 450", price: 100, stock: 10},
    {Id: 3, name: "Suitcase 650", price: 350, stock: 2},
    {Id: 4, name: "Suitcase 1050", price: 550, stock: 5}
]

function getItemById(id){
    for (const item of listProducts) {
      if (item.Id === id) return item;
    }
  }
  

async function reserveStockById(itemId, stock) {
    await clientSet(itemId, stock);
}

async function getCurrentReservedStockById(itemId) {
    return await clientGet(itemId);
}

const app = express()

app.get('/list_products', (req, res) => {
    res.json(listProducts);
})

app.get('/list_products/:itemId', async (req, res) => {
    const id = Number(req.params.itemId)
    const item = getItemById(id)
    const reservedStock = await getCurrentReservedStockById(id);
    if (item) {
        item.reserveStock = (reservedStock) ? reservedStock : 0;
        res.json(item);
    }
    res.status(404).json({"status":"Product not found"})
})

app.get('/reserve_product/:itemId', async (req, res) => {
    const id = Number(req.params.itemId)
    const item = getItemById(id);
    if ( !item ) res.json({"status":"Product not found"})

    const stock = await getCurrentReservedStockById(id)
    if ( !stock ) {
        res.json({"status":"Not enough stock available","itemId":id})
    }
    reserveStockById(id)
    res.json({"status":"Reservation confirmed","itemId":id})
})

app.listen(1245);
