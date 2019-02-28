<template>
  <div class="ruterComponentWrapper">
    <!-- <iframe src="https://mon.ruter.no/monitor/3010370/Forskningsparken/"></iframe> -->
  </div>
</template>

<script>
// var url = "https://mon.ruter.no/monitor/3010370/Forskningsparken/"
// import gql from 'apollo-boost';
// const testQuery = gql{
//   {
//     authors{
//       name
//       id
//     }
//   }
// };
import axios from 'axios';
//59600 - forskningsparken
//59894 - sagene
export default {
  name: 'Ruter',
  methods:{
    async getRealTimeData () {
      try {
        const res = await axios.post(
          'https://api.entur.io/journey-planner/v2/graphql', {
          query: `{ 
              stopPlace(id:"NSR:StopPlace:59600"){ 
                id 
                name
                estimatedCalls(timeRange: 72100, numberOfDepartures: 10){
                  realtime
                  aimedArrivalTime
                  aimedDepartureTime
                  expectedArrivalTime
                  expectedDepartureTime
                  actualArrivalTime
                  actualDepartureTime
                  date
                  forBoarding
                  forAlighting
                  serviceJourney {
                    journeyPattern {
                      line {
                        id
                        name
                        transportMode
                      }
                    }
                  }
                }
                
                } 
            }`
        })
        // this.example1 = res.data.data.language
        console.log(res)
        // console.log(`${this.getGraphQlTime()}`);
      } catch (e) {
        console.log('err', e)
      }
    },
    //Ikke nodvendig? fjern evt.
    getGraphQlTime(){
      // 2019-02-28T13:00:00+0200
      var d = new Date();
      var ret = '';
      ret += d.getFullYear().toString();
      ret += '-';
      ret += this.zeroPadding(d.getMonth()+1, 2);
      ret += '-';
      ret += this.zeroPadding(d.getDate(), 2);
      ret += 'T';
      ret += this.zeroPadding(d.getHours(), 2);
      ret += ':' + this.zeroPadding(d.getMinutes(), 2);
      ret += ':' + this.zeroPadding(d.getSeconds(), 2);
      ret += '+0200';
      return ret;

    },
    zeroPadding: function(num, digit) {
        var zero = '';
        for(var i = 0; i < digit; i++) {
            zero += '0';
        }
        return (zero + num).slice(-digit);
    }
  },
  beforeMount(){
    // getHTML()
    this.getRealTimeData();
    
  }
  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.ruterComponentWrapper{
    background: #333;
}

</style>
