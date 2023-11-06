<template>
  <div class="grid-container">
    <div class="title">
      <garage-dialog
        v-if="garageDialog"
        :garage="garage"
        @update="garage = $event"
        @close="garageDialog = false"
      />
      <div class="garage">
        <h1>Garage {{ garage.name }}</h1>
        <h4>
          Brand: {{ garage.brand }} - Country: {{ garage.postal_country }}
        </h4>
      </div>
      <div>
        <div>
          <button
            type="button"
            class="btn btn-primary"
            @click="garageDialog = true"
          >
            Edit Garage
          </button>
          <button type="button" class="btn btn-danger" @click="deleteGarage">
            Delete Garage
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import GarageDialog from './garage-dialog';

export default {
  components: { GarageDialog },
  data() {
    return {
      garage: {
        name: '',
        brand: '',
        postal_country: '',
      },
      garageDialog: false,
    };
  },
  methods: {
    getGarage() {
      console.log(this.$route.params.id);
      const url = '/garages/?garage=' + this.$route.params.id;
      console.log(url);
      fetch(url)
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          this.garage = data;
        });
    },
    toggleEdit() {
      this.editing = !this.editing;
    },
    deleteGarage() {
      console.log('deleting..');
      fetch('/garages/?garage=' + this.garage.id, {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ garage: this.garage.id }),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          this.$router.push({ name: 'home' });
        });
    },
  },
  mounted() {
    this.getGarage();
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

.title {
  grid-area: title;
  display: flex;
  align-items: center; /* Vertical align the elements to the center */
  justify-content: space-between;
  text-align: start;
}

.title .list-group {
  grid-area: garage-list;
}
</style>
