<template>
  <main class="container">
    <div
      class="d-flex justify-content-center align-items-start"
      style="height: 80vh"
    >
      <div>
        <div class="card" style="width: 20rem">
          <h5 class="m-3">{{ question.question_text }}</h5>
          <ul class="list-group list-group-flush">
            <li class="list-group-item text-center" v-for="choice in choices">
              {{ choice.choice_text }}
              <span class="badge text-bg-danger"
                >{{ choice.votes }} vote<span v-if="choice.votes > 1"
                  >s</span
                ></span
              >
            </li>

            <li class="list-group-item d-flex justify-content-center">
              <div class="btn-group" style="width: 20rem">
                <a class="btn btn-outline-primary" href="/polls"
                  >All questions</a
                >
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </main>
</template>
<script>
import sileo from "sileo";
// import router from "@/routes";

const Choice = new sileo.Model("polls", "choices");
const Question = new sileo.Model("polls", "questions");

export default {
  data() {
    return {
      question_id: this.$route.params.question_id,
      question: {},
      choices: [],
    };
  },
  methods: {
    async getQuestion() {
      Question.objects.get(this.question_id).then((data) => {
        this.question = data;
        console.log(data);
        Choice.objects.filter({ question: this.question.pk }).then((data) => {
          console.log(data);
          this.choices = data;
        });
      });
    },
  },
  async created() {
    await this.getQuestion();
  },
};
</script>
