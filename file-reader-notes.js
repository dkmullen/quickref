function readSingleFile(evt) {
  //Retrieve the first (and only!) File from the FileList object
  let f = evt.target.files[0]; 

  if (f) {
    let r = new FileReader();
    r.onload = (e) => { 
      let contents = e.target.result;
      // alert( "Got the file.n" 
      //       +"name: " + f.name + "n"
      //       +"type: " + f.type + "n"
      //       +"size: " + f.size + " bytesn"
      //       + "starts with: " + contents.substr(1, contents.indexOf("n"))
      // );  
      console.log(contents)
    }
    r.readAsText(f);
  } else { 
    alert("Failed to load file");
  }
}









// openFileSelector() {
//     let fileSelector = document.createElement('input');
//     fileSelector.type = 'file';
//     fileSelector.accept = '.ix.license';
//     fileSelector.click();
// }

  openFileSelector() {
    let fileSelector = document.createElement('input');
    fileSelector.type = 'file';
    fileSelector.onchange = this.onChange;
    fileSelector.click();
  }

  onChange(event) {
    console.log(event)
  }

                <!-- <textarea 
                    name="licenseText"
                    class="form-control"
                    [(ngModel)]="licenseText"
                    ></textarea> -->
