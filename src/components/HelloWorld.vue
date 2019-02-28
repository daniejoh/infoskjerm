<template>
  <div class="hello">
    <Test/>
    <Ruter/>

    <!-- <Dagens/> -->
    <h1>Din Component her</h1>
    <h1>Din Component her</h1>
    <h1>Din Component her</h1>

  
  </div>
</template>

<script>
import Test from './Test.vue';
import Ruter from './Ruter.vue';
import Dagens from './Dagens.vue';
export default {
  name: 'HelloWorld',
  components: {
    Test,
    Ruter,
    Dagens
  }
  
  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.hello {
  /* margin: 0 auto; */
  width: 100%;
  height: 90vh;
  font-size: 40px;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-auto-rows: minmax(50px, auto);
  /* grid-column-gap: 3px;
  grid-row-gap: 3px; */
  grid-gap: 10px;
  overflow: hidden;
  min-width: 0;
  min-height: 0;
  
}

h1{
  overflow: hidden;
}
</style>
