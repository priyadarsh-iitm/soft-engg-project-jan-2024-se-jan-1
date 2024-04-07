<template>
    <div class="container">
        <h3 style="color:aqua; text-align: center;">Admin portal</h3>
        <div class="topic-container">
            <h3><RouterLink :to="{name: 'manageUsers'}" style="color: #fff;">Manage Users</RouterLink></h3>
        </div>
        <br/>
        <hr/>
        <div class="topic-container">
            <h3><RouterLink :to="{name: 'manageFAQ'}" style="color: #fff;">View New Suggestions for FAQ</RouterLink></h3>
        </div>
        <br/>
        <hr/>
        <div class="topic-container">
            <h3><RouterLink :to="{name: 'manageFlaggedPosts'}" style="color: #fff;">View Flagged Posts</RouterLink></h3>
        </div>
    </div>
</template>

<style>
body {
  background-color: #222; /* Dark background color for the entire page */
  color: #fff; /* White text color */
}

.container {
  padding: 20px; /* Add padding for content */
}

.topic-container {
  padding: 10px;
}

.topic-container h3 {
  margin: 0;
}

.topic-container h3:hover {
  color: #ff4444; /* Highlight color on hover */
}

hr {
  border-color: #555; /* Dark border color */
}
</style>

<script>
//import router from '@/router';

export default {
    name: "DashboardAdminComponent",
    data() {
        return {
            
        };
    },
    
    
}
</script>

<style scoped>
.topic-container {
    margin: 33px 63px;
}

.upvote {
    font-size: 20px;
}

.ticket-title {
    font-weight: bold;
    font-size: 25px;
}

.btn a {
    color: rgb(255, 255, 255);
    text-decoration: none;
}

a {
    color: rgb(0, 0, 0);
    text-decoration: none;
}
</style>