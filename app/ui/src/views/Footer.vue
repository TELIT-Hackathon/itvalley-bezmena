<template>
  <div>
    <div class="footer">
      Copyright © 2022 | <!--{{ $t("Other.Footer") }}--> 
      <a href="mailto:orsolyovadianka@gmail.com">Full stack developer <img src="../images/linkedin-logo.jpg" class="contacts-icons"> | </a>
      <a href="mailto:orsolyovadianka@gmail.com"> Front end developer <img src="../images/gmail_icon.jpg" class="contacts-icons"></a>
      
    </div>
  </div>
</template>

<style>
.footer{
  justify-content: center;
  background-color: #dceeea;
	padding: 25px 0;
	position: fixed;
	z-index: -1000;
  left: 0;
  right: 0;
	bottom: 0;
  display: flex;
}

.contacts-icons{
  width: 1.5rem;
  height: 1.5rem;
  position: relative;
  top: 6px;
}

.footer a{
  margin-top: -7px;
  margin-left: 6px;
}
</style>

<script>
</script>