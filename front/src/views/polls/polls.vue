<template>
  <nav
    class="navbar navbar-expand-lg bg-primary mb-3 px-5"
    data-bs-theme="dark"
  >
    <div class="container-fluid">
      <a class="navbar-brand" href="/polls">Polls</a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a
              class="nav-link"
              href="http://127.0.0.1:8000/admin"
              target="_blank"
              >Admin</a
            >
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <router-view></router-view>
</template>
<script></script>
