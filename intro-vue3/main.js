const { createApp, ref, computed, provide } = Vue;

const app = createApp({
  setup() {
    const cart = ref([]);
    const premium = ref(true);
    const details = ref(["50% cotton", "30% wool", "20% polyester"]);

    const addToCart = ({ id }) => cart.value.push(id);
    const removeFromCart = () => cart.value.length > 0 && cart.value.pop();

    provide("cart", cart);

    return {
      cart, premium, details, 
      addToCart, removeFromCart, 
    };
  },
});
