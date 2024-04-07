<template>
    <div class="container dark-mode">
        <div class="topic-container">
            <h3 style="color:aqua; text-align: center;">Manager portal</h3>
            <h3><RouterLink :to="{name: 'AddAdmins'}" style="color: #fff;">Add Admins</RouterLink></h3>
        </div>
        <br/>
        <hr style="border-color: #fff;" />
    </div>
</template>

<script>
//import router from '@/router';

export default {
    name: "DashboardManagerComponent",
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