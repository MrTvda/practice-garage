<template>
  <modal
    :title="garage.id ? 'Edit garage' : 'New garage'"
    @close="$emit('close')"
  >
    <form class="form-col">
      <label>
        Name
        <input v-model="garage.name" />
      </label>
      <label>
        Brand
        <input v-model="garage.brand" />
      </label>
      <label>
        Country
        <input v-model="garage.postal_country" />
      </label>
    </form>
    <template v-slot:footer>
      <button class="btn btn-primary" @click="save()">
        Save
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
      required: false,
      default() {
        return {};
      },
    },
  },
  name: 'garage-dialog',
  components: {
    Modal,
  },
  data() {
    return {};
  },
  methods: {
    save() {
      fetch('/garages/', {
        method: this.garage.id ? 'PUT' : 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.garage),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(JSON.stringify(data));
          this.$emit('update', data);
          this.$emit('close');
        });
    },
  },
};
</script>

<style scoped>
label {
  margin-bottom: 1.5rem;
}
</style>
