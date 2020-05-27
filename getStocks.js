const Alpaca = require('@alpacahq/alpaca-trade-api')
const express = require('express')
const bodyParser = require('body-parser');

const alpaca = new Alpaca({
	keyId: "PKRZGWVR3MNK33BT8R4A",
	secretKey:"gqkhQtP5/OSd1iOqFc8qvbSN8HJmftXhDS1IWap5",
	paper: true,
	usePolygon: false
})


function getStockPrices(symbolList) {
	const barset = alpaca.getBars(
		'1Min',
		symbolList,
		{	
			limit: 1000,
			start:'2020-05-12T09:30:00-04:00',
			end: '2020-05-1209:30:00-04:00',
		}
	)

	return barset
}


const app = express();
app.use(bodyParser.json());
app.use(express.static('public'))
app.get('/watchlist', (req, res) => getStockPrices(req.query.symbols).then((barset) => {
								res.send(barset);
							})
		)

app.listen(3000, () => {
	console.log("Listening on port 3000");
	
})





