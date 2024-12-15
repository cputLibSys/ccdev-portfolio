import { Directive, OnChanges, OnInit, Input, ElementRef, OnDestroy, SimpleChanges } from "@angular/core";
import { MathlibService } from "./mathlib.service";
import { take, takeUntil } from "rxjs/operators";
import { Subject} from "rxjs";

@Directive({
  selector: '[appMath]'
})
export class MathlibDirective implements OnInit, OnChanges, OnDestroy {

  @Input() private appMath: string;
  private alive$ = new Subject<boolean>();
  private readonly el: HTMLElement;

  constructor(private mathService: MathlibService, private elementRef: ElementRef) {
    this.el = elementRef.nativeElement;
  }

  ngOnInit() {
    this.render();
  }

  ngOnChanges(changes: SimpleChanges) {
    if(changes && changes['appMath'] && changes['appMath'].currentValue) {
      this.render();
    }
  }

  private render() {
    this.mathService.ready().pipe(
      take(1),
      takeUntil(this.alive$)
    ).subscribe(() => this.mathService.render(this.el, this.appMath));
  }

  ngOnDestroy() {
    this.alive$.next(false);
  }
 
}
