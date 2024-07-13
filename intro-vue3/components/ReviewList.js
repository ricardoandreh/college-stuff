app.component("review-list", {
  props: {
    reviews: {
      type: Array,
      required: true,
    },
  },
  template: `
    <div class="review-container">
    <h3>Reviews:</h3>
      <ul>
        <li v-for="review, index in reviews" :key="index">
          <strong>{{ review.name }}</strong> avaliou com {{ review.rating }} estrelas
          <br/>
          <em>"{{ review.review }}"</em>
          <br/>
          Recomendado: <u>{{ review.recommended }}</u>
          <br/>
        </li>
      </ul>
    </div>`,
});
