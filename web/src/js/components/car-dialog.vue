<template>
  <modal :title="car.id ? 'Edit car' : 'New car'" @close="$emit('close')">
    <form class="form-col">
      <label>
        Garage
        <p>{{ garage.name }}</p>
      </label>
      <label>
        Brand
        <input v-model="car.brand" />
      </label>
      <label>
        Name
        <input v-model="car.name" />
      </label>
    </form>
    <template #footer>
      <button type="submit" class="btn btn-primary" @click="save()">
        Save
      </button>
      <button type="button" class="btn btn-danger" @click="$emit('close')">
        Cancel
      </button>
    </template>
  </modal>
</template>

<script>
import Modal from './modal';
export default {
  props: {
    garage: {
      type: Object,
      required: true,
    },
    car: {
      type: Object,
      required: false,
      default() {
        return {
          garage_id: this.garage.id,
        };
      },
    },
  },
  name: 'car-dialog',
  components: {
    Modal,
  },
  data() {
    return {};
  },
  methods: {
    save() {
      fetch('/garages/' + this.garage.id + '/cars', {
        method: this.car.id ? 'PUT' : 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.car),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(JSON.stringify(data));
          this.$emit('update', data);
          this.$emit('close');
        });
    },
  },
  mounted() {},
};
</script>

<style scoped>
label {
  margin-bottom: 1.5rem;
}
</style>
