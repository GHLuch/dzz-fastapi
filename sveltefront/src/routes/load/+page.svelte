<script>
  import { goto } from "$app/navigation";
  import { task_id } from "$lib/task_store"
  let fileVar;
  let container;
  let image;
  let placeholder;
  let showImage = false;
  function clean(){
    fileVar = null;
    image.setAttribute("src", "");
    
  }
  
  function onChange() {
    const file = fileVar[0];

    if (file) {
      showImage = true;

      const reader = new FileReader();
      reader.addEventListener("load", function () {
        image.setAttribute("src", reader.result);
      });
      reader.readAsDataURL(file);

      return;
    }
    showImage = false;
  }
  async function postForm() {
    const formData = new FormData();

    console.log(fileVar);
    formData.append("image", fileVar[0]);
    try {
      const res = await fetch("/api/image/upload", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();
      console.log(data); // Do something with the response data
      $task_id = data.task_id
      goto("/result")
    } catch (error) {
      console.error("Error uploading file:", error);
    }
  }
</script>

<div class="row">
  <div class="column-file">
    <p>Загрузите изображение</p>

    <form class="py-2" on:submit|preventDefault={postForm}>
      <div class="column-file-loading">
        <div class="example-1">
          <div class="form-group">
            <label class="label">
              <input
                type="file"
                bind:files={fileVar}
                on:change={onChange}
                accept="image/*"
              />
              <div
                bind:this={container}
                style="width: 650px; height: 350px; margin: 10px;"
              >
                {#if showImage}
                  <img
                    bind:this={image}
                    style="width: 100%; height: 100%; object-fit: cover;"
                    src=""
                    alt="Preview"
                  />
                {:else}
                  <span bind:this={placeholder}
                    >Нажимите, чтобы загрузить изображение</span
                  >
                {/if}
              </div>
            </label>
          </div>
        </div>
      </div>
      <div class="column-file-box">
        <nav class="nav-max-770px">
          <p>
            <button on:click|preventDefault={clean} class="file-button-2">Очистить</button>
          </p>
          <p>
            <button type="submit" class="file-button-4">Перейти к этапу обработки</button
            >
          </p>
        </nav>
        <nav class="nav-min-770px">
          <p>
            <button on:click|preventDefault={clean} class="file-button-2">Очистить</button>
            <button type="submit" class="file-button-4">Перейти к этапу обработки</button
            >
          </p>
        </nav>
      </div>
    </form>
  </div>
</div>
