<template>
  <div>
    <div class="footer">
      Copyright © 2022 | <!--{{ $t("Other.Footer") }}--> 
      <a href="https://www.linkedin.com/in/horvathmar">Marek Horvath <img src="../images/linkedin-logo.jpg" class="contacts-icons"> | </a>    
      <a href="https://www.linkedin.com/in/matus-toth-58848b238/">Matúš Tóth <img src="../images/linkedin-logo.jpg" class="contacts-icons"> | </a>    
      <a href="https://www.facebook.com/tomas.kormanik.7">Tomáš Kormaník <img src="../images/linkedin-logo.jpg" class="contacts-icons"> | </a>    
      <a href="https://www.facebook.com/tomas.gordon.sk">Tomáš Gordoň <img src="../images/linkedin-logo.jpg" class="contacts-icons"> | </a>    
      <a href="https://www.linkedin.com/in/daniel-chovanec-b5844616a">Daniel Chovanec <img src="../images/linkedin-logo.jpg" class="contacts-icons"> | </a>    
    </div>
  </div>
</template>

<style>
.footer{
  justify-content: center;
  background-color: #020381;
  color: white;
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

.footer a:link,.footer a:visited{
  color: white;
}
</style>

<script>
</script>