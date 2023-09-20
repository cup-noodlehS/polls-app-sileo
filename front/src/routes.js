import { createRouter, createWebHistory } from "vue-router";
import Polls from "./views/polls/polls.vue";
import PollsDetails from "./views/polls/details.vue";
import PollsIndex from "./views/polls/index.vue";
import PollsNew from "./views/polls/new.vue";
import PollsResults from "./views/polls/results.vue";
import PageNotFound from "./views/pageNotFound.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/polls",
      component: Polls,
      children: [
        { path: "", component: PollsIndex },
        { path: "new", component: PollsNew },
        { path: ":question_id", component: PollsDetails },
        { path: ":question_id/results", component: PollsResults },
      ],
    },
    {
      path: "/:catchAll(.*)",
      component: PageNotFound,
    },
  ],
});

export default router;
