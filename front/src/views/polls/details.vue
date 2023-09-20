<template>
  <main class="container">
    <div
      class="d-flex flex-column justify-content-start align-items-center"
      style="height: 80vh"
    >
      <div class="d-flex justify-content-center">
        <div class="card" style="width: 20rem">
          <h5 class="m-3">{{ question.question_text }}</h5>
          <p v-if="noChoices" class="text-center">No Choices</p>
          <ul class="list-group list-group-flush">
            <li class="list-group-item" v-for="(choice, index) in choices">
              <input
                type="radio"
                name="choicesGroup"
                :id="`choice${index}`"
                :value="index"
                v-model="choiceSelected"
              />
              <label :for="`choice${index}`" class="ms-2">{{
                choice.choice_text
              }}</label>
            </li>
            <div class="m-1 d-flex justify-content-center">
              <div class="btn-group" style="width: 20rem">
                <button
                  class="btn btn-primary"
                  v-if="!noChoices"
                  @click="vote"
                  :disabled="choiceSelected == null"
                >
                  Vote
                </button>
                <a href="/polls" class="btn btn-outline-primary">Cancel</a>
              </div>
            </div>
            <a @click="deleteQuestion" class="btn btn-outline-danger m-1">
              Delete
            </a>
          </ul>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import sileo from "sileo";
import router from "@/routes";

const Choice = new sileo.Model("polls", "choices");
const Question = new sileo.Model("polls", "questions");

export default {
  data() {
    return {
      question_id: this.$route.params.question_id,
      question: {},
      choices: [],
      noChoices: false,
      choiceSelected: null,
    };
  },
  methods: {
    async deleteQuestion() {
      await Question.objects
        .delete({ pk: this.question_id })
        .then((data) => {
          console.log(data);
          router.push({ path: `/polls` });
        })
        .catch((e) => {
          console.log("error");
          console.log(e);
        });
    },
    async getQuestion() {
      Question.objects.get(this.question_id).then((data) => {
        this.question = data;
        console.log(data);
        Choice.objects.filter({ question: this.question.pk }).then((data) => {
          console.log(data);
          if (data.length != 0) {
            this.choices = data;
          } else {
            this.noChoices = true;
          }
        });
      });
    },
    async vote() {
      const choice = this.choices[this.choiceSelected];
      console.log(choice);
      Choice.objects
        .update(
          { pk: choice.pk },
          {
            question: this.question.pk,
            votes: choice.votes + 1,
            choice_text: choice.choice_text,
          }
        )
        .then((data) => {
          console.log(data);
          router.push({ path: `/polls/${this.question_id}/results` });
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
  async created() {
    await this.getQuestion();
  },
};
</script>
