<template>
    <div class="container dark-mode">
        <div class="topic-container">
            <div class="container" v-for="(category, index) in categories" :key="index">
                <h3 style="color: #fff;"> {{ category  }}</h3>
                <br>
                <div v-for="t in tickets" :key="t.ticket_id">
                    <div class="container" v-if="t.is_approved && t.category==category">
                        <div class="row">
                            <div class="col-md-10">
                                <p class="ticket-title">
                                    <RouterLink :to="{ name: 'response', params: { ticketId: t.ticket_id } }" style="color: #fff;">
                                        {{ t.title }}
                                    </RouterLink>
                                </p>
                                <p style="color: #fff;">{{ t.description }}</p>
                            </div>
                            <div class="col-md-2">
                                <div class="row">
                                    <button class="btn upvote" @click="increaseVote(t.ticket_id, t.number_of_upvotes)"
                                        style="color: #fff;">^<br>{{ t.number_of_upvotes }}</button>
                                </div>
                                <div class="row" v-if="this.$store.state.role==3">
                                    <div class="btn-group">
                                        <button type="button" class="btn dropdown-toggle" data-bs-toggle="dropdown"
                                            style="color: #fff;">
                                            Options
                                        </button>
                                        <ul class="dropdown-menu">
                                            <button class="dropdown-item text-center" @click="removeFromFAQ(t.ticket_id)"
                                                style="color: #fff;"> Remove From FAQ </button>
                                            <button class="dropdown-item text-center" data-bs-toggle="modal"
                                                data-bs-target="#faqModal" @click="this.selected_ticket = t.ticket_id; this.selected=t.category"
                                                style="color: #fff;"> Change Category </button>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <hr />
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- Modal -->
    <div class="modal fade" id="faqModal" tabindex="-1" aria-labelledby="faqModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="faqModalLabel" style="color: #fff;">Please choose the appropriate category</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <select v-model="selected" style="color: #000;">
                        <option disabled value="">Please select one</option>
                        <option v-for="(c, index) in categories" :key="index">{{ c }}</option>
                    </select>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-success" data-bs-dismiss="modal" @click="changeCategory()">Submit</button>
                </div>
            </div>
        </div>
    </div>
    <div class="container" v-if="this.$store.state.role==3">
        <div class="text-center">
            <button class="btn btn-warning" data-bs-toggle="modal" data-bs-target="#categoryModal">
                <b>New Category</b>
            </button>
        </div>
        <!-- Modal -->
        <div class="modal fade" id="categoryModal" tabindex="-1" aria-labelledby="categoryModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="categoryModalLabel" style="color: #fff;">Please add the appropriate category name</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="form-group">
                            <label style="color: #fff;">Category: </label>
                            <input type="text" v-model="cat" class="form-control" placeholder="Enter Category" autocomplete="off"
                                required>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-success" data-bs-dismiss="modal" @click=" addCategory()">Submit</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
.dark-mode {
    background-color: #222; /* Dark background color */
    color: #fff; /* White text color */
}

.heading {
    color: #fff; /* White text color for button text */
}

.card {
    background-color: #333; /* Darker background color for cards */
    color: #fff; /* White text color for card content */
}

.form-group label {
    color: #fff; /* White text color for form labels */
}

.form-control {
    background-color: #444; /* Darker background color for form inputs */
    color: #fff; /* White text color for form inputs */
    border-color: #555; /* Dark border color for form inputs */
}

.btn-primary {
    background-color: #007bff; /* Blue button color */
    border-color: #007bff; /* Blue border color */
    color: #fff; /* White text color */
}

.btn-primary:hover {
    background-color: #0056b3; /* Darker blue button color on hover */
    border-color: #0056b3; /* Darker blue border color on hover */
}
</style>

<script>
import axios from 'axios';

export default {
    name: "FaqComponent",
    data() {
        return {
            tickets: [],
            categories: [],
            selected_ticket: null,
            selected: null,
            cat: null
        };
    },
    async created() {
        var res2 = await axios.get('/api/category');
        this.categories = res2.data.data;
        await axios.get("/api/faq").then((res) => {
            // console.log(res.data.data);
            for (var i = 0; i < res.data.data.length; i++) {
                this.tickets.push(res.data.data[i]);
            }
        });
    },
    methods: {
        async addCategory() {
            var res = await axios.post('/api/category', {
                category: this.cat
            });
            console.log(res);
            this.$router.go();
        },
        async changeCategory() {
            var res = await axios.patch('/api/faq', {
                ticket_id: this.selected_ticket,
                is_approved: true,
                category: this.selected
            });
            console.log(res);
            this.$router.go();
        },
        async removeFromFAQ(ticket_id) {
            var res = await axios.patch('/api/faq', {
                ticket_id: ticket_id,
                is_approved: false
            });
            console.log(res);
            this.$router.go();
        },
        increaseVote(ticket_id, upVotes) {
            var data = {
                ticket_id: ticket_id,
                number_of_upvotes: upVotes + 1
            }
            data = JSON.stringify(data);
            axios.patch("/api/ticketAll", data).then((res) => {
                console.log(res);
            }).catch((err) => {
                console.log(err);
            });
            this.$router.go();
        },
    }
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