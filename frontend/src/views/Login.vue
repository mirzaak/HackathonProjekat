<template>
<div class="container-fluid d-flex align-items-center justify-content-center vh-100 row">


<div class=" vh-100 d-flex align-items-center justify-content-center">
  <form >
  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label text-light">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">

  </div>
  <div class="mb-3">
    <label for="exampleInputPassword1" class="form-label text-light">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1">
  </div>
  <div class="mb-3 form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1">
    <label class="form-check-label text-light" for="exampleCheck1">Remember me!</label>
  </div>
  <p class="text-light">Not a member? <a href="#" class="text-decoration-none"> <router-link class="text-decoration-none" to="/register">Register</router-link></a></p>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>

</div>

</div>

  </template>
  <script>
  
  </script>
  <style>
  </style>
  