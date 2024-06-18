<script>
  import { task_id } from "$lib/task_store";
  import Spinner from "svelte-spinner";
  import { Lightbox } from "svelte-lightbox";
  let socket;
  let status = "Не запущено";
  let found_objects = null;
  let title_text = "Не запущено";
  let stage = "notstarted";
  async function startTask() {
    try {
      const res = await fetch("/api/image/start_task/" + $task_id, {
        method: "POST",
        body: null,
      });
      title_text = "Запуск обработки...";
      const data = await res.json();
      socket = new WebSocket(
        "wss://" +
          location.hostname +
          (location.port ? ":" + location.port : "") +
          "/api/image/status/" +
          $task_id,
      );
      socket.addEventListener("message", (message) => {
        const data = JSON.parse(message.data);
        console.log(data);
        status = data.status;
        stage = data.stage;
        title_text = data.title_text;
        if (stage == "finished") {
          found_objects = data.found_objects;
        }
      });
      console.log(data); // Do something with the response data
    } catch (error) {
      console.error("Error uploading file:", error);
    }
  }
</script>

<div class="row">
  <div class="column-result">
    <p>{title_text}</p>
    <div class="column-result-box">
      <nav>
        <a class="result-box-button">
          <button class="result-button-2">{status}</button>
          <button class="result-button-2" on:click={startTask}>Начать</button>
        </a>
      </nav>
    </div>
  </div>
</div>

<table class="prcessed-img-table">
  <tr>
    <td>
      <div class="prcessed-img">
        {#if stage=="process"}
        <Spinner size="50" speed="750" color="#A82124" thickness="2" gap="40" />
        {:else if stage=="finished"}
        <Lightbox><img src="/api/image/result/{$task_id}" /></Lightbox>
        {:else}
        Не запущено
        {/if}
      </div>
    </td>
    {#if found_objects}
    <td>
      {#if found_objects.length > 0}
    Найдено обьектов на изображении:
      {#each found_objects as found_object}
      	<p>{found_object.name}: {found_object.count}</p>
      {/each}
      {:else}
      На изображении не найдено обьектов
      {/if}
    </td>
    {/if}
  </tr>
</table>
