<template>
  <div class="grid-container">
    <div class="title">
      <car-dialog
        v-if="carDialog"
        :garage="garage"
        @update="updateCarsList"
        @close="carDialog = false"
      />
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
    <div class="list-group">
      <div class="title">
        <div>
          <h2>Cars</h2>
        </div>
        <div>
          <button
            type="button"
            class="btn btn-success"
            @click="carDialog = true"
          >
            Add Car
          </button>
        </div>
      </div>
      <ul>
        <li v-for="car in cars" :key="car.id">
          <car :garage="garage" :car="car"></car>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import GarageDialog from './garage-dialog';
import CarDialog from './car-dialog';
import Car from './car';

export default {
  components: { GarageDialog, CarDialog, Car },
  data() {
    return {
      garage: {
        name: '',
        brand: '',
        postal_country: '',
      },
      cars: [
        {
          name: '',
          brand: '',
          garage_id: 0,
        },
      ],
      garageDialog: false,
      carDialog: false,
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
    deleteGarage() {
      console.log('deleting garage... ' + this.garage.id);

      const garageJson = { garage: this.garage.id };
      const garageJsonStr = JSON.stringify(garageJson);
      const garageJsonParse = JSON.parse(garageJsonStr);

      console.log(garageJsonStr);
      console.log(garageJsonParse);
      // console.log(JSON.stringify({ garage: this.garage.id }));
      fetch('/garages/?garage=' + this.garage.id, {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' },
        body: garageJsonStr,
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          this.$router.push({ name: 'home' });
        });
    },
    getCars() {
      console.log('Getting cars..');
      const url = '/garages/' + this.$route.params.id + '/cars';
      console.log(url);
      fetch(url)
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          this.cars = data;
        });
    },
    updateCarsList(data) {
      this.cars.push(data);
    },
  },
  mounted() {
    this.getGarage();
    this.getCars();
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
    'car-list';
}

.title {
  grid-area: title;
  display: flex;
  align-items: center; /* Vertical align the elements to the center */
  justify-content: space-between;
  text-align: start;
}

.title .list-group {
  grid-area: car-list;
}

.list-group .title {
  display: flex;
  justify-content: space-between;
}

.list-group .title {
  display: flex;
  justify-content: space-between;
}

ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
}

ul li {
  background-color: white;
  padding: 1.5rem;
  margin-bottom: 1rem;
  border-color: #ccc;
  border: 1px 1px 1px 1px;
  border-style: solid;
  border-radius: 10px;
}
</style>
