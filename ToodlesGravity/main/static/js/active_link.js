$(document).ready(function () {
    $(function () {
        var current_page_URL = location.href;

        $("a").each(function () {

            if ($(this).attr("href") !== "#") {

                var target_URL = $(this).prop("href");

                if (target_URL == current_page_URL) {
                    $("nav a").removeClass("active");
                    $(this).addClass("active");

                    return false;
                }
            }
        });
    });
});
