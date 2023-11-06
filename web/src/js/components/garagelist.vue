<template>
  <div class="grid-container">
    <div class="title">
      <h1>Garages</h1>
      <button type="button" class="btn" @click="garageDialog = true">
        Add garage
      </button>
      <garage-dialog
        v-if="garageDialog"
        @update="updateList"
        @close="garageDialog = false"
      />
    </div>
    <table class="table table-striped">
      <thead>
        <tr>
          <th>Garage</th>
          <th>Brand</th>
          <th>Country</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="g in garageList" :key="g.id">
          <td>
            <a :href="'/#/garages/' + g.id">{{ g.name }}</a>
          </td>
          <td>{{ g.brand }}</td>
          <td>{{ g.postal_country }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import GarageDialog from './garage-dialog';

export default {
  name: 'garage-list',
  components: { GarageDialog },
  data() {
    return {
      garageList: [],
      garageDialog: false,
    };
  },
  methods: {
    load() {
      $.ajax({
        type: 'GET',
        url: `/garages/`,
        contentType: 'application/json',
        timeout: 60000,
      })
        .then((data) => {
          console.log(data);
          this.garageList = data;
        })
        .always(() => {
          // this.loading = false
        });
    },
    updateList(data) {
      this.garageList.push(data);
    },
    remove(id) {
      console.log(id);
      this.garageList = this.garageList.filter((val) => val.id !== id);
    },
  },
  created: function() {
    this.load();
  },
};
</script>

<style scoped>
.grid-container {
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 60px 1fr;
  grid-gap: 8px;
  grid-template-areas:
    'title'
    'garage-list';
}

.list-group {
  grid-area: garage-list;
}
.add-garage {
  margin: 4px;
}

.title {
  grid-area: title;
  display: flex;
  align-items: center; /* Vertical align the elements to the center */
}

h1 {
  margin: 0;
}

button {
  margin-left: auto; /* Push this element to the right */
}

td {
  text-align: start;
}
</style>
