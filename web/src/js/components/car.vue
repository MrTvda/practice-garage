<template>
  <div>
    <car-dialog
      v-if="carDialog"
      :garage="garage"
      :car="car"
      @close="carDialog = false"
    />
    <div class="cars-list">
      <div>
        <h4>{{ car.brand }} {{ car.name }}</h4>
      </div>
      <div>
        <button type="button" class="btn btn-primary" @click="carDialog = true">
          Edit Car
        </button>
        <button type="button" class="btn btn-danger" @click="deleteCar(car.id)">
          Delete Car
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import CarDialog from './car-dialog';

export default {
  components: { CarDialog },
  props: {
    garage: {
      type: Object,
      required: true,
    },
    car: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      cars: [],
      carDialog: false,
    };
  },
  methods: {
    deleteCar(id) {
      console.log('Deleting car...');
      fetch('/cars?car=' + id, {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ car: id }),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          this.cars = this.cars.filter((car) => car.id !== id);
        });
    },
  },
};
</script>

<style scoped>
.cars-list {
  display: flex;
  justify-content: space-between;
}
</style>
