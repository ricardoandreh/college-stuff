const { createApp, ref } = Vue;

createApp({
  setup() {
    const [product, description] = [
      ref("Boots"), 
      ref("description: that's a great pair of socks!")
    ];

    return {
      product, description
    }
  }
}).mount("#app");
