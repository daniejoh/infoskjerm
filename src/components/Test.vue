<template>
    <div class="componentWrapper">
        <h1>{{time}}</h1>
    </div>
</template>

<script>

export default {
  name: 'Test',
  data(){
      return {
          time: ''
      }
  },
  methods: {
      setDate: function(){
          var d = new Date();
          this.time = this.zeroPadding(d.getHours(), 2) + ':'
           + this.zeroPadding(d.getMinutes(), 2) + ':' 
           + this.zeroPadding(d.getSeconds(), 2);
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
      setInterval(this.setDate, 1000);
  }
  
}

</script>

<style scoped>
.componentWrapper{
    background: #333;
    color: aquamarine;
}

</style>
