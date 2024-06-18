<script>
import './main_loading_result.css'
</script>
<header>
    <div>
        <a href="/" class="logo">GYM</a>
    </div>
    <nav class="header-max-770">
        <a href="/"><button>Главная</button></a>
    </nav>
    <nav class="header-min-770">
        <a><button>
            <div class="header-menu"></div>
            <div class="header-menu"></div>
            <div class="header-menu"></div>
        </button></a>
    </nav>
</header>
<slot>
</slot>
<footer>
    <div>
        <a href="/" class="logo-footer"> © 2024 “GYM”</a>
    </div>
    <nav>
        <img src="/image 7.png" alt="img" class="img-7-footer">
        <img src="/image 6.png" alt="img" class="img-6-footer">
    </nav>
</footer>
