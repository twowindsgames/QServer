<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated  class="glossy bg-blue-grey-6
">
      <q-toolbar  >
        <q-btn
          flat
          dense
          :to="'/storage' "
          round

          aria-label="Menu"
          icon="menu"
        >
        
        </q-btn>

        <q-btn
          flat
          dense
          :to="'/storage/mix' "
          round

          aria-label="Menu"
          icon="menu"
        >

        </q-btn>

        <q-toolbar-title >
          Storage v1.001
           <q-btn
          flat
          dense
          round

          label="Stor"
          @click="leftDrawerOpen = !leftDrawerOpen"
          aria-label="Menu"
        />
        </q-toolbar-title>

        <div>Quasar v{{ $q.version }}</div>
      </q-toolbar>
    </q-header>


    <q-page-container class="bg-blue-grey-4

" >
       <q-page-container >

      <section  class="section ">
        <q-page>
          <router-view  />
        </q-page>
      </section>
    </q-page-container>
    </q-page-container>
  </q-layout>
</template>

<script>
import { ref } from 'vue'


export default {

  name: 'LayoutDefault',



  setup () {


    // calling here; equivalent to when component is created

    return {

      leftDrawerOpen: ref(false)
    }
  }
}
</script>
