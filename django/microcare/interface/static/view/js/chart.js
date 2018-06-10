//Sampel Pie Doughnut Chart
var PieDoughnutChartSampleData = [
    {
        value: 651,
        color:"#F7F000",
        highlight: "#F4F726",
        label: "Exposto"
    },
    {
        value: 791,
        color: "#000000",
        highlight: "#696969",
        label: "Noite"
    },
    {
        value: 1,
        color: "#46BFB0",
        highlight: "#5AD3D0",
        label: "Chuva"
    }
];

 window.onload = function() {
    window.PieChartSample = new Chart(document.getElementById("pie-chart-sample").getContext("2d")).Pie(PieDoughnutChartSampleData,{
   responsive:true});
 };