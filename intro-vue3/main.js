const { createApp, ref } = Vue;

const app = createApp({
  setup() {
    const onSale = ref(true);
    const inStock = ref(true);
    const inventory = ref(100);
    const product = ref("Socks");
    const image = ref("./assets/images/socks_green.jpg");
    const details = ref(["50% cotton", "30% wool", "20% polyester"]);
    const url = ref("https://www.linkedin.com/in/ricardoandreh/");
    const sizes = ref(["S", "M", "L", "XL"]);
    const variants = ref([
      { id: 2234, color: "green" }, 
      { id: 2235, color: "blue" }, 
    ]);

    return {
      product, image, url, 
      inStock, inventory, onSale, 
      details, variants, sizes, 
    }
  }
});
