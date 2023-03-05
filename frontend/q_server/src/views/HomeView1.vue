<template>
  <div class="home  "
 >

 <q-btn
          flat
          dense
          round
          @click="allDelete"
          aria-label="Menu"
          icon="delete"
        />
      <q-list  v-for="result in results" v-bind:key="result.id" >
      <q-item clickable    >
     <b >{{result.get_absolute_points}}:  {{result.percent}}%  {{result.sum}} SET:</b> {{result.settings}}
      <em> {{result.day_count}} </em >

      </q-item>
    </q-list>
  </div>
</template>

<script>
// @ is an alias to /src

import axios from 'axios'

export default {
  name: 'HomeView',
  data() {
    return {
      results: [],
    }
  },
mounted() {
    this.getAllResults()
  },


   methods: {
   getAllResults() {
      axios
          .get('/api/storage/results/mix')
          .then(response => {
           // this.results = response.data.sort((a, b) => { return b.get_absolute_points - a.get_absolute_points;});
            this.results= response.data
          })
          .catch(error => {
            console.log(error);
          })
    },
      allDelete() {
      axios
          .delete('/api/storage/results/mix')
          .then(response => {
            console.log(response);

          })
          .catch(error => {
            console.log(error);
          })
    },
      detailDelete(id) {
      axios
          .delete('/api/storage/mix/detail',{params: {result_id: id},})
          .then(response => {
            console.log(response);

          })
          .catch(error => {
            console.log(error);
          })
    },


   }
}
</script>
