<template>
  <div class="alert" v-if="format == 1">
    <span class="closebtn" onclick="this.parentElement.style.display='none';"
      >&times;</span
    >
    {{ messg }}
  </div>

  <div class="alert2" v-if="format == 2">
    <span class="closebtn" onclick="this.parentElement.style.display='none';"
      >&times;</span
    >
    {{ messg }}
  </div>
</template>


<script>
export default {
  name: "Notification",
  props: {
    messg: String,
    format: Number,
  },
};
</script>


<style scoped>
/* The alert message box */
.alert {
  padding: 20px;
  background-color: #f44336; /* Red */
  color: white;
  margin-bottom: 15px;
}

/* The alert message box */
.alert2 {
  padding: 20px;
  background-color: #56f436; /* Red */
  color: white;
  margin-bottom: 15px;
}

/* The close button */
.closebtn {
  margin-left: 15px;
  color: white;
  font-weight: bold;
  float: right;
  font-size: 22px;
  line-height: 20px;
  cursor: pointer;
  transition: 0.3s;
}

/* When moving the mouse over the close button */
.closebtn:hover {
  color: black;
}
</style>