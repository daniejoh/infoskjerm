<template>
    <div class="DagensComponentWrapper">
        <h3><div class="DagensTitle">Dagens</div> er {{dagens}}</h3>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: "Dagens",
    data(){
        return{
            dagens: ''
        }
    },
    beforeCreate(){
        axios.get("http://localhost:8484")
            .then((data)=>{
                console.log(data);
                this.dagens = data.data
            })
            .catch(err =>{
                console.log(err);
            })
    }
}
</script>

<style scoped>
h3{
    font-size: 3vh;
}
.DagensTitle{
    color: #f442bf;
}
</style>
