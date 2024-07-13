const { createApp, ref, computed } = Vue;

const app = createApp({
  setup() {
    const cart = ref(0);
    const premium = ref(true);
    const details = ref(["50% cotton", "30% wool", "20% polyester"]);

    return {
      cart, premium, details
    };
  },
});
