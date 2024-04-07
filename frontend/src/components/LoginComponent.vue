<template>
  <div class="container dark-mode">
    <h1 class="text-center">IITM TICKETING SYSTEM</h1>
    <h2 class="text-center" style="color:aqua;">Welcome to Login</h2>
    <form @submit.prevent="loginUser">
      <div class="form-group">
        <label style="color: #fff;"><b>Email</b></label>
        <input type="text" v-model="email" class="form-control" placeholder="Enter Email" autocomplete="off" required />
      </div>
      <div class="form-group">
        <label style="color: #fff;"><b>Password</b></label>
        <input type="password" v-model="password" class="form-control" placeholder="Password" autocomplete="off" required />
      </div>
      <button type="submit" class="btn btn-primary btn-dark">Submit</button>
      <br>
      <br>
      <p class="text" style="margin-top:10px">
        Forgot Password?<RouterLink to="/changePassword" style="color: #ff4444;"><b>Click Here</b></RouterLink>
      </p>
    </form>
  </div>
</template>

<style>
.dark-mode {
  background-color: #222; /* Dark background color */
}

.dark-mode h1 {
  color: #fff; /* White text color */
}

.dark-mode label {
  color: #fff; /* White text color */
}

.dark-mode input[type="text"],
.dark-mode input[type="password"] {
  background-color: #333; /* Darker background color for input fields */
  color: #fff; /* White text color */
  border-color: #555; /* Dark border color */
}

.dark-mode .btn-primary {
  background-color: #007bff; /* Blue button color */
  border-color: #007bff; /* Blue border color */
  color: #fff; /* White text color */
}

.dark-mode .btn-primary:hover {
  background-color: #0056b3; /* Darker blue button color on hover */
  border-color: #0056b3; /* Darker blue border color on hover */
}

.dark-mode .text {
  color: #fff; /* White text color */
}
</style>


<script>
import axios from "axios";
export default {
  name: "LoginComponent",
  data() {
    return {
      email: "",
      password: ""
    };
  },
  methods: {
    loginUser(e) {
      e.preventDefault();
      console.log(this.email, this.password);
      axios.post("/login", {
        email: this.email,
        password: this.password
      }).then(res => {
        console.log(res);
        if (res.status == 200) {
          localStorage.setItem("token", res.data.token);
          localStorage.setItem("user_id", res.data.user_id);
          this.$store.dispatch("user_id", res.data.user_id);
          localStorage.setItem("role", res.data.role);
          this.$store.dispatch("role", res.data.role);
          axios.defaults.headers.common["secret_authtoken"] = res.data.token;
          if(res.data.role == "1"){
            this.$router.push("/dashboard");
          }
          else if(res.data.role == "3"){
            this.$router.push("/dashboard");
          }
          else if(res.data.role == "2"){
            this.$router.push("/dashboard");
          }
          else if(res.data.role == "4"){
            this.$router.push("/dashboard");
          }
        } else {
          alert(res.data.message);
        }
      }).catch(err => {
        console.log(err);
      });
    },
  }
}
</script>

<style scoped>
.container {
  /* border: #40cbea solid 2px;
  border-radius: 20px; */
  font-family: "Muli", sans-serif;
  margin-top: 50px;
  width: 50%;
  padding: 20px 40px;
  margin-left: auto;
  margin-right: auto;
}

.container h1 {
  text-align: center;
  margin-bottom: 30px;
  font-size: 50px;
}

.form-group {
  margin-bottom: 25px;
}

label {
  font-size: 20px;
  font-weight: 500;
  color: #333;
  margin-bottom: 5px;
}
</style>
