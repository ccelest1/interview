# notes
- ReefnBid = eccomerce platform for Stripe for conducting transactions
    * Stripe = 3rd party api
1. How can we use stripe in performing capabilities for ReefnBid as Eccomerce Marketplace

Stripe - looking at the API
    * payment methods - rest endpoints
        -

- Flow of the app
    * User sets up their payment methods
    * Store presents items to purchase
    * User wants to purchase items and then go through proper transaction flow
        - item is in bag/cart -> user proceeds to pay
        - payment action occurs (eventListener)
        - stripe will handle payment and return json object that has payment method id and a status of either succesful transaction or nonsuccesful w/ other helpful metadata
    * (sync) User gets pending status
    * User gets end status about if their payment is successful or not
        - Happy path: user gets success notification and receives product/estimation of when product will be delivered
            * Transaction is recorded
        - Bad path: user gets notification about non-succesful payment -> redirect back to the store

- Stripe terminology
    * products
    * customers
    * session

- Demonstrate the correct tax process -> important for admins who are non-technical

- Sales tax using Stripe
```js

// tax package - imports ongoing taxes
// state, federal, local (these can all be different)
// explain destination charges, complaint regarding taxes
/*
grab the shipping address
figure out rates based on the above and apply the correct rates
incorporating state, county, city, federal
rates must be updated quarterly

compliance - keep tax records for 3-7 years
*/
function get_rates_by_address(address){
    // return all accompaying tax rates - as an dictionary object
    {
        'city_tax_rate': x%
        ...
    }
}

let rates = get_rates_by_address()
calc_taxes(rates,...)
function calc_taxes(...args){

}

stripe.paymentIntents.create({
// amount transacted below on 1st line
     amount: 100,
     transfer_data: {
       destination: 'acct_seller',
       amount: 95, // Seller gets $95, platform keeps $5
     }
   });
```

------

- Create a clone of tiktok
* Features: Video player with algorithmic reccomend videos
    * Main thing: Worrying it being a vertical video player
        - Main things:
            * Videos ingest
            * Vertical Player

* Video Vertical Player
```js
// three main comps: video ref, progress, playing interaction
const videoRef = //url -> s3 store (allows for cloud storage of videos)
// we want to take chunks out of the url

async const video_playback = (play_interaction: clickEvent, chunk:url, progress:timestamp) => {

    if(play_interaction === 'play'){
        let current_video_chunk = await videoRef(chunk)
        let current_chunk = chunk[progress]
    }else{
        break //pause interaction
    }
}
```

* Videos Ingest
```js
async const upload_video =( s3: string, codex: clips[]){
    let video = clips[]
    let presigned_url = ''
    for(let clip of video){
        try{
        let upload = await `s3.presigned_url${id}`
        }catch(e){
             console.error(e)
        }

    }
}
```
