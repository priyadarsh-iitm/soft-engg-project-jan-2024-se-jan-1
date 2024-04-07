<template>
    <nav class="navbar navbar-expand-lg bg-dark" style="width: 100%;">
        <div class="container-fluid">
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0" v-if="user_id">
                    <li class="nav-item">
                        <router-link to="/dashboard" class="navbar-brand"><b style="font-weight: bold;">IITM TICKETING SYSTEM</b></router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to="/allTicket" class="nav-link active" aria-current="page"><b>All
                            Tickets</b></router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to="/faq" class="nav-link active" aria-current="page"><b>FAQ</b></router-link>
                    </li>
                    <li class="nav-item">
                        <a href="http://localhost:4200/" class="nav-link active" aria-current="page"
                            target="_blank"><b>Discourse</b></a>
                    </li>
                </ul>
                <form class="d-flex" role="search" v-if="user_id">
                    <button class="btn btn-outline-light" type="submit" @click="logout">Logout</button>
                </form>
            </div>
        </div>
    </nav>
</template>

<style>
.navbar {
  background-color: #222; /* Dark background color for navbar */
  color: #fff; /* White text color */
}

.nav-link,
.navbar-brand {
  color: #fff !important; /* White text color for links */
}

.navbar-brand b {
  font-weight: bold; /* Make navbar-brand text bold */
}

.navbar-toggler-icon {
  background-color: #fff; /* White color for navbar toggler icon */
}

.btn-outline-light {
  color: #fff; /* White text color for outline button */
  border-color: #fff; /* White border color for outline button */
}

.btn-outline-light:hover {
  background-color: #ff4444; /* Red background color on hover */
  color: #fff; /* White text color on hover */
  border-color: #ff4444; /* Red border color on hover */
}
</style>

<script>
import axios from 'axios';
import { mapGetters } from "vuex";
export default {
    name: 'NavBar',
    methods: {
        logout() {
            localStorage.removeItem('token');
            localStorage.removeItem('user_id');
            localStorage.removeItem('role');
            this.$store.dispatch("user_id", null);
            this.$store.dispatch("role", null);
            delete axios.defaults.headers.common["secret_authtoken"];
            this.$router.push('/');

        }
    },
    computed: {
        ...mapGetters(["user_id"]),
    },
}
</script>
