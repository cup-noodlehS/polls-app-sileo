<template>
  <main>
    <div class="d-flex justify-content-center">
      <div class="card">
        <div class="card-header">Add Question</div>
        <ul class="list-group list-group-flush">
          <li class="list-group-item">
            <div class="input-group">
              <span class="input-group-text" id="basic-addon3">Question</span>
              <input
                type="text"
                class="form-control"
                id="basic-url"
                v-model="questionText"
                autocomplete="off"
              />
            </div>
          </li>
          <li class="list-group-item" v-if="choiceCount > 0">
            <p class="ms-2">Choices</p>
            <ul>
              <li v-for="(choice, index) in choices">
                {{ choice }}
                <button
                  @click="removeChoice(index)"
                  style="
                    border-radius: 50%;
                    border: none;
                    background: none;
                    color: red;
                  "
                >
                  ⓧ
                </button>
              </li>
            </ul>
          </li>
          <li class="list-group-item">
            <div class="input-group mb-2">
              <span class="input-group-text" id="basic-addon3"
                >Choice {{ choiceCount + 1 }}</span
              >
              <input
                type="text"
                class="form-control"
                id="basic-url"
                aria-describedby="basic-addon3 basic-addon4"
                v-model="newChoice"
                @keyup.enter="addChoice"
              />
              <button
                class="btn btn-primary"
                @click="addChoice"
                :disabled="newChoice.length == 0"
              >
                Add
              </button>
            </div>
          </li>
          <li class="list-group-item d-flex justify-content-end">
            <button
              class="btn btn-success me-1"
              v-if="questionText != '' && choiceCount > 0"
              @click="save"
            >
              Save
            </button>
            <a href="/polls" class="btn btn-danger">Cancel</a>
          </li>
        </ul>
      </div>
    </div>
  </main>
</template>

<script>
import sileo from "sileo";
import router from "@/routes";

const currentDateTime = new Date();
const Choice = new sileo.Model("polls", "choices");
const Question = new sileo.Model("polls", "questions");

export default {
  data() {
    return {
      questionText: "",
      choiceCount: 0,
      choices: [],
      newChoice: "",
      question_id: null,
    };
  },
  methods: {
    addChoice() {
      this.choices.push(this.newChoice);
      this.newChoice = "";
      this.choiceCount++;
    },
    removeChoice(index) {
      this.choices.splice(index, 1);
      this.choiceCount--;
    },
    async save() {
      console.log(this.questionText);
      Question.objects
        .create({
          question_text: this.questionText,
          pub_date: currentDateTime.toISOString(),
        })
        .then((data) => {
          console.log(data);
          this.question_id = data.pk;
          this.choices.map((choice) => {
            Choice.objects
              .create({
                choice_text: choice,
                question: data.pk,
                votes: 0,
              })
              .then((data) => {
                console.log(data);
                router.push({ path: `/polls/${this.question_id}` });
              });
          });
        })
        .catch((e) => {
          console.log(e);
          console.log("errorrr");
        });
    },
  },
};
</script>
