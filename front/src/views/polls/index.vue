<template>
  <main class="container">
    <div class="d-flex justify-content-center flex-wrap">
      <div class="mx-3 mb-3">
        <div class="card" style="width: 20rem">
          <div class="row align-items-center">
            <h5 class="m-3 col-7">Polls</h5>
            <!-- <a
                href="{% url 'polls:deleteset' set.id %}"
                class="btn btn-danger col-3"
                style="height: 38px; border-radius: 18px"
                >Delete</a
              > -->
          </div>
          <ul class="list-group list-group-flush">
            <li
              class="list-group-item d-flex justify-content-between"
              @click="gotoPage(quesiton.pk)"
              v-for="(quesiton, index) in questions"
            >
              <a
                @click="gotoPage(quesiton.pk)"
                class="text-decoration-none question-text"
                >{{ index + 1 }}. {{ quesiton.question_text }}</a
              >
              <a
                @click="gotoPage(quesiton.pk)"
                class="btn btn-outline-primary mx-2 position-relative"
                style="height: 38px"
                >Answer</a
              >
            </li>
            <div class="list-group list-group-flush">
              <button
                class="btn btn-primary text-center p-2"
                @click="gotoNewQuestion"
              >
                Add Question
              </button>
            </div>
          </ul>
        </div>
      </div>
    </div>
  </main>
</template>
<script>
import router from "@/routes";
import sileo from "sileo";

const Question = new sileo.Model("polls", "questions");

export default {
  data() {
    return {
      questions: [],
    };
  },
  methods: {
    async getQuestions() {
      this.questions = await Question.objects.filter();
    },
    gotoPage(pk) {
      router.push({ path: `/polls/${pk}` });
    },
    gotoNewQuestion() {
      router.push({ path: "/polls/new" });
    },
  },
  async created() {
    await this.getQuestions();
  },
};
</script>
<style scoped>
.question-text {
  color: black;
}
.add {
  color: white !important;
}
</style>
