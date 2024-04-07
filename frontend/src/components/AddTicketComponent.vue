<template>
    <div class="container dark-mode">
        <!-- <div class="row justify-content-center"> -->
            <div class="col">
                <h4 class="text-center" style="color: aqua; text-align: center;">Add Ticket</h4>
                <form @submit.prevent="addCard">
                    <div class="form-group">
                        <label style="color: #fff;">Title</label>
                        <i class="bi bi-patch-question-fill" data-toggle="tooltip" data-placement="top" title="As you type the title, similar queries will appear on the right. Please read them before creating a new ticket."></i>
                        <input type="text" v-model="title" class="form-control" placeholder="Enter title" autocomplete="off" required />
                    </div>
                    <div class="form-group">
                        <label style="color: #fff;">Description</label>
                        <textarea v-model="description" class="form-control" placeholder="Enter description" autocomplete="off" required rows='10'></textarea>
                    </div>
                    <div class="form-group form-check">
                        <input type="checkbox" id="postOnDiscourse" v-model="postOnDiscourse" class="form-check-input">
                        <label for="postOnDiscourse" class="form-check-label" style="color: #fff;">Post on Discourse</label>
                    </div>
                    <button type="submit" class="btn btn-success">Submit</button>
                </form>
            </div>
            <div class="col-sm">
                <div class="container overflow-auto">
                    <p v-if="results" style="color: #fff;">Please look at the following similar tickets before posting a new query</p>
                    <div class="search-result" v-for="(result, index) in results" :key="index">
                        <h3>
                            <RouterLink :to="{ name: 'response', params: { ticketId: result.ticket_id } }">
                                <div v-html="result._highlightResult.title.value" style="color: #fff;"></div>
                            </RouterLink>
                        </h3>
                        <div v-html="result._highlightResult.description.value" style="color: #fff;"></div>
                    </div>
                </div>
            </div>
        </div>
    <!-- </div> -->
</template>

  
<script>
import axios from "axios";
export default {
    name: "AddTicketComponent",
    data() {
        return {
            title: "",
            description: "",
            results: null,
            postOnDiscourse: false
        };
    },
    watch: {
        title: async function (val) {
           let url = 'https://RRBO0FF8YF-dsn.algolia.net/1/indexes/sociogrammers_app/query'
           // eslint-disable-next-line
           let config = {
                headers: {
                    'X-Algolia-Application-Id': 'RRBO0FF8YF',
                    'X-Algolia-API-Key': localStorage.getItem('alg-key'),
                        }
                    }
            // eslint-disable-next-line
            let data = {
                'query': val
            }
            var instance = axios.create();
            delete instance.defaults.headers.common['secret_authtoken'];
            const response = await instance.post(url, data, config)
            this.results = response.data.hits
        }
    },
    methods: {
        async addCard() {
            var data = {
                title: this.title,
                description: this.description,
                number_of_upvotes : 0,
                is_read: false,
                is_open: true,
                is_offensive: false,
                is_FAQ: false,
                on_discourse: this.postOnDiscourse
            };
            data = JSON.stringify(data);
            console.log(data);
            await axios.post("/api/ticket",data, {
            headers: {
                    // "secret_authtoken": localStorage.getItem("token"),
                    "Content-Type": "application/json"
            }
            }).then((res) => {
                console.log(res);
                if (res.status == 200) {
                    alert("Ticket Added Successfully");
                    this.$router.push("/dashboard");
                } else {
                    alert(res.data.message);
                }
            }).catch((err) => {
                console.log(err);
            });       
            
        }
    },
}
</script>
  
<style scoped>
.container {
    font-family: "Muli", sans-serif;
    /* display: flex;
     */
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 75vh;
    overflow: hidden;
    margin-top: 75px;
}

label {
    font-size: 1.2rem;
    font-weight: 500;
    margin-bottom: 5px;
}

h1 {
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 2rem;
}

.form-group {
    margin-bottom: 1.5rem;
}
.topic-container {
    margin: 33px 63px;
}

.ticket-title {
    font-weight: bold;
    font-size: 25px;
}

</style>
  