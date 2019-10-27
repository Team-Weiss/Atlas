<template>
  <transition enter-active-class="slide-in-right" leave-active-class="slide-out-right">
    <div class="notification column" v-if="proceed">
      <p style="font-weight: bold; font-size: 1.4em;">Info</p>
      <p style="font-size: 1.2em;">The selected operation was started successfully</p>
    </div>
  </transition>
</template>

<script>
export default {
  props: ['proceed']
}
</script>

<style lang="scss" scoped>
.notification {
  position: fixed;
  bottom: 2em;
  right: 0;
  padding: 2em;
  color: #FFF;
  border-left: 2px solid #e8bc44;
  background-color: #29313d;
}

.slide-in-right {
	-webkit-animation: slide-in-right 0.5s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
	        animation: slide-in-right 0.5s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
}
@keyframes slide-in-right {
  0% {
    -webkit-transform: translateX(1000px);
            transform: translateX(1000px);
    opacity: 0;
  }
  100% {
    -webkit-transform: translateX(0);
            transform: translateX(0);
    opacity: 1;
  }
}

.slide-out-right {
	-webkit-animation: slide-out-right 0.5s cubic-bezier(0.550, 0.085, 0.680, 0.530) both;
	        animation: slide-out-right 0.5s cubic-bezier(0.550, 0.085, 0.680, 0.530) both;
}
@keyframes slide-out-right {
  0% {
    -webkit-transform: translateX(0);
            transform: translateX(0);
    opacity: 1;
  }
  100% {
    -webkit-transform: translateX(1000px);
            transform: translateX(1000px);
    opacity: 0;
  }
}

</style>