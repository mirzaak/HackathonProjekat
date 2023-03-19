<template>
  <nav class="navbar navbar-expand-lg fixed-top">
  <div class="container-fluid p-2 ps-5 pe-5">
    <h3 href="#" class="text-decoration-none m-0"> <router-link class="text-decoration-none" to="/"><h3><img class="img-fluid m-0" style="max-width: 80px;" src="../assets/logo.png" alt=""></h3></router-link></h3>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse ms-3" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0 d-flex">
        <li class="nav-item d-flex align-items-center">
          <a href="#" class="text-decoration-none fs-5 text-white" > <router-link class="text-decoration-none text-white" to="/dashboard">Dashboard</router-link></a>
        </li>
      </ul>
        <a href="#" class="text-decoration-none fs-5 text-white"> <router-link class="text-decoration-none text-white" to="/login"><button type="button" class="btn btn-outline-light fs-5">Login</button></router-link></a>
    </div>
  </div>
</nav>
</template>

<script>
export default {

}
</script>

<style>
.navbar {
    background:transparent !important;
}
</style>