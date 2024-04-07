<template>
    <div class="container dark-mode">
        <div class="topic-container">
            <h3 style="color: #fff;">ADD ADMIN BY EMAIL ID</h3>
        </div>
        <br />
        <form v-on:submit="addUser">
            <div class="form-group">
                <label style="color: #fff;">Enter Email ID</label>
                <input type="text" class="form-control" v-model="emailID" required />
            </div>
            <br />
            <div class="form-group">
                <label style="color: #fff;">Enter password</label>
                <input type="password" class="form-control" v-model="password" required />
            </div>
            <br />
            <button class="btn btn-lg btn-primary" type="submit">Submit</button>
        </form>
        <hr style="border-color: #555;" />
    </div>
</template>

<script>
//import router from '@/router';
import axios from 'axios';
export default {
    name: "AddAdminsComponent",
    data() {
        return {
            emailID: "",
            password:"",
            roleID: 3,
        };

    },
    methods: {
        async addUser(x) {
            // console.log(this.response)
            x.preventDefault();
            console.log(this.emailID);
            let c = this.emailID
            var data = { email_id: c,password:this.password, role_id: this.roleID };
            console.log(c);
            data = JSON.stringify(data);
            console.log("Data is :")
            console.log(data);
            await axios.post("/api/user", data).then((res) => {
                alert("User has been successfully added.")
                this.$router.go();
                console.log(res)
            }).catch((err) => {
                console.log(err);
            });
            
        },
        
    }
}
</script>
<style scoped>
.topic-container {
    margin: 33px 63px;
}
.form-group {
    margin-bottom: 1.5rem;
}
</style>