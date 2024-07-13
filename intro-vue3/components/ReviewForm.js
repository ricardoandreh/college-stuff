app.component("review-form", {
  emits: ["review-submitted"],
  setup(props, { emit }) {
    const name = ref("");
    const review = ref("");
    const rating = ref(null);
    const recommended = ref(null);

    const onSubmit = () => {
      if (
        name.value === "" ||
        review.value === "" ||
        rating.value === null ||
        recommended.value === null
      ) {
        alert("Review incompleta. Por favor, preencha todos os campos.");
        return;
      }

      const productReview = {
        name: name.value,
        review: review.value,
        rating: rating.value,
        recommended: recommended.value,
      };

      emit("review-submitted", productReview);

      name.value = "";
      review.value = "";
      rating.value = null;
      recommended.value = null;
    };

    return {
      name, review, 
      rating, onSubmit, 
      recommended, 
    };
  },
  template: `
    <form class="review-form" @submit.prevent="onSubmit">
      <h3>Deixe uma review</h3>
      <label for="name">Nome:</label>
      <input id="name" v-model="name">

      <label for="review">Review:</label>      
      <textarea id="review" v-model="review"></textarea>

      <label for="rating">Nota:</label>
      <select id="rating" v-model.number="rating">
        <option>5</option>
        <option>4</option>
        <option>3</option>
        <option>2</option>
        <option>1</option>
      </select>

      <label for="recommended">Recomendaria esse produto?</label>
      <select id="recommended" v-model="recommended">
        <option>Com certeza</option>
        <option>Sim</option>
        <option>Talvez</option>
        <option>Não</option>
        <option>Jamais</option>
      </select>

      <input class="button" type="submit" value="Submit">
    </form>`,
});
