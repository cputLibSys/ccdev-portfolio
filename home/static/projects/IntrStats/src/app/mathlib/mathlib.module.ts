import { NgModule } from "@angular/core";
import { MathlibDirective } from "./mathlib.directive";
import { MathlibService } from "./mathlib.service";

@NgModule({
  declarations: [MathlibDirective],
  exports: [MathlibDirective],
  providers: [MathlibService]
})
export class MathlibModule {}
