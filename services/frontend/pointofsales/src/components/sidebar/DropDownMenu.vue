<script setup>
import DownMenu from './DownMenu.vue';
defineProps(['title'])


function sideBarItemCollapse(id, event) {
    let expanded = event.target.getAttribute('aria-expanded').toLocaleLowerCase() == 'true' ? true : false;
    let el = document.getElementById(id);
    expanded ? el.classList.remove('show') : el.classList.add('show');
    event.target.setAttribute('aria-expanded', !expanded);
}
</script>

<template>
    <a class="nav-link" href="javascript:void(0)" @click="sideBarItemCollapse('collapseProducts', $event)"
        data-toggle="collapse" role="button" aria-expanded="false" aria-controls="collapseProducts">
        {{title}}
    </a>
    
    <DownMenu id="collapseProducts"></DownMenu>
</template>

<style>

</style>